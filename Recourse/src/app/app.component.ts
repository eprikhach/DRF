import {Component, OnInit} from '@angular/core';
import {AuthService} from './shared/auth.service';
import {User} from "./shared/user";
import {MatMenuModule} from '@angular/material/menu';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {
    currentUser: User = new User()
    token = this.authService.getToken()

    constructor(
        public authService: AuthService,
    ) {
        this.authService.getUserProfile().subscribe((res: any) => {
            this.currentUser = res;
        });
    }


    isTeacher() {
        return this.currentUser.user_status == 'TE'
    }

    logout() {
        this.authService.doLogout()
    }

    ngOnInit(): void {
    }

}