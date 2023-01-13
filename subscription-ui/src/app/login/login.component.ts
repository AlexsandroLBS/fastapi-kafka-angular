import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { of } from 'rxjs';
import { IUser } from '../interface/user';
import { SubsctriptionService } from '../services/subsctription-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private subsService: SubsctriptionService, private router: Router) { }

  public userName: string = '';
  public userPassword: string = '';
  public errorMessage: string = '';

  public sessionUser: any = ''
  ngOnInit(): void {
  }

  getLogin(){
    let user: IUser ={
      full_name: this.userName,
      password: this.userPassword
    }

    this.subsService.login(user).subscribe((data) => {
      this.sessionUser = data;
      if(this.sessionUser.response.error){
        this.errorMessage = this.sessionUser.response.error
        } 
      else{
        sessionStorage.setItem('user', this.userName);

        this.router.navigateByUrl('user/'+this.userName)
      }
    })
  }
}
