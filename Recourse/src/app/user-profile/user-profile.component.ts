import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {AuthService} from '../shared/auth.service';
import { User } from "../shared/user";


@Component({
    selector: 'app-user-profile',
    templateUrl: './user-profile.component.html',
    styleUrls: ['./user-profile.component.sass'],
})
export class UserProfileComponent implements OnInit {
    currentUser: User = new User()
    token = this.authService.getToken()

    constructor(
        public authService: AuthService,
    ) {
        this.authService.getUserProfile().subscribe((res: any) => {
            this.currentUser = res;
        });
    }

    ngOnInit() {
    }
}