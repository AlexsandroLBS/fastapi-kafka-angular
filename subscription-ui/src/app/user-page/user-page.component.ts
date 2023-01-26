import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { SubsctriptionService } from '../services/subsctription-service.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.css']
})
export class UserPageComponent implements OnInit {

  constructor(private route: ActivatedRoute, private subsService: SubsctriptionService, private router: Router) { 
    this.route.params.subscribe(params => this.user = params['user']);
  }

  private userStatus: number = 0;
  public accessAllowed: boolean = false;
  public user: string = '';
  public disabledBtn: boolean = false;
  public subMessage: string = '';
  public btnMessage: string = 'Assinar';
  public isLoading: boolean = false;

  ngOnInit(): void {
    this.verifyAccess();
    if(this.accessAllowed){
      this.refreshData()
    }
  }

  private verifyAccess(){
    if(this.user == sessionStorage.getItem('user')){
      this.accessAllowed = true;
    }
    else{
      this.accessAllowed = false;
    }
  }

  public refreshData(){
    this.subsService.getStatus(this.user)
      .subscribe((data)=> {
        this.userStatus = data.status
        sessionStorage.setItem('status', data.status.toString())
        if(this.userStatus == 1 || this.userStatus == 3){
          this.subMessage = 'Sua inscrição está ativa.'
          this.disabledBtn = false
        }
        else if(this.userStatus == 2){
          this.subMessage = 'Sua assinatura foi cancelada.'
          this.btnMessage = 'Reassinar'
          this.disabledBtn = true
        }
        else{
          this.subMessage = 'Você não possui assinatura.'
          this.btnMessage = 'Assinar'
          this.disabledBtn = true
        }
      })
  }

  public sendSubNotification(){
    if(this.btnMessage = 'Assinar'){
      this.subsService.sendNotification({
        action: 'SUBSCRIPTION_PURCHASED',
        full_name: this.user
      }).subscribe((data) => {if(data){
          this.isLoading = true,
          setTimeout(() => this.reload(), 3000)
      }})
    } 
    else{
      this.subsService.sendNotification({
        action: 'SUBSCRIPTION_RESTARTED',
        full_name: this.user
      }).subscribe((data) => {if(data){
          this.isLoading = true,
          setTimeout(() => this.reload(), 3000)
      }})
    }
  }

  public sendCancelNotification(){
    this.subsService.sendNotification({
      action: 'SUBSCRIPTION_CANCELLED',
      full_name: this.user
    }).subscribe((data) => {if(data){ 
        this.isLoading = true,
        setTimeout(() => this.reload(), 3000)
      }})
  }

  private reload(){
    console.log('veio aqui')
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
    this.router.onSameUrlNavigation = 'reload';
    this.router.navigate(['./'], {
      relativeTo: this.route
    })
  }
}
