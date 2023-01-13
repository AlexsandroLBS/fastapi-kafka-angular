import { Component, OnInit } from '@angular/core';
import { IUser } from '../interface/user';
import { SubsctriptionService } from '../services/subsctription-service.service';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {

  constructor(private subsService: SubsctriptionService) { }

  public userName: string = '';
  public userPassword: string = '';
  public confirmPassword: string = '';
  public errorMessage: string = '';
  public successMessage: string = '';

  ngOnInit(): void {
  }

  showMessage(flag:boolean, message:string){

    if(flag){
      this.errorMessage = message;
    }
    else{
      this.successMessage = message;
    }
  }

  verifyPassword() : boolean{
    if(this.confirmPassword.length>0){
      if(this.userPassword != this.confirmPassword){
      this.showMessage(true,'As senhas devem ser iguais');
      return false;
      }
      else{
        this.errorMessage = '';
        return true;
      }
    }
    else{
      this.errorMessage = '';
      return false
    }
  }

  verifyMessage(res: string) {

    if(res == 'usuario ja existe'){
      this.showMessage(true,"Nome de usuário já existe")
    }
    else if(res == 'usuario inserido'){
      console.log('veio aqui')
      this.showMessage(false,"Usuário criado!")
    }
  }

  createAccount(){
    let user: IUser ={
      full_name: this.userName,
      password: this.userPassword
    }
    if (this.verifyPassword()){
      this.subsService.createAccount(user).subscribe((data) =>
        this.verifyMessage(data.toString())
      )
    }
  }
}
