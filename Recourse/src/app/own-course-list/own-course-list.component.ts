import {Component, OnInit} from '@angular/core';
import {Course} from "../shared/ticket";
import {AuthService} from "../shared/auth.service";
import {FormBuilder} from "@angular/forms";
import {Router} from "@angular/router";
import {TicketService} from "../shared/ticket.service";
import {UserService} from "../shared/user.service";
import {Observable} from "rxjs";


@Component({
    selector: 'app-own-course-list',
    templateUrl: './own-course-list.component.html',
    styleUrls: ['./own-course-list.component.sass']
})
export class OwnCourseListComponent implements OnInit {
    courseList!: Course[];
    course!: Course;

    constructor(public authService: AuthService,
                public fb: FormBuilder,
                public router: Router,
                public ticketService: TicketService,
                private userService: UserService) {

        this.ticketService.getOwnTicket().subscribe((res: any) => {
                this.courseList = res
                console.log(this.courseList)
            }
        )
    }

    ngOnInit(): void {

    }

    getCourse(id: string) {
        this.router.navigate([`course/${id}`])
        // this.course = this.ticketService.getOwnTicket(id)
    }


}
