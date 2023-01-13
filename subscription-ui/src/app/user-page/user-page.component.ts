import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.css']
})
export class UserPageComponent implements OnInit {

  constructor(private route: ActivatedRoute) { 
    this.route.params.subscribe(params => this.user = params['user']);
  }

  public accessAllowed: boolean = false;
  public user: string = '';

  ngOnInit(): void {
    this.verifyAccess();
  }

  verifyAccess(){
    if(this.user == sessionStorage.getItem('user')){
      this.accessAllowed = true;
    }
    else{
      this.accessAllowed = false;
    }
  }
}
