import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../shared/auth.service";
import {ActivatedRoute, Router} from "@angular/router";
import {TicketService} from "../shared/ticket.service";
import {UserService} from "../shared/user.service";
import {User} from "../shared/user";
import {COMMA, ENTER} from "@angular/cdk/keycodes";

@Component({
    selector: 'app-edit-course',
    templateUrl: './edit-course.component.html',
    styleUrls: ['./edit-course.component.sass']
})
export class EditCourseComponent implements OnInit {
    courseName!: FormGroup;
    courseDescribe!: FormGroup;
    currentUser: User = new User()
    separatorKeysCodes: number[] = [ENTER, COMMA];
    thisCourseId!: string;

    constructor(public authService: AuthService,
                public fb: FormBuilder,
                public router: Router,
                public ticketService: TicketService,
                private route: ActivatedRoute,) {
    }

    ngOnInit(): void {
        this.courseName = this.fb.group({
            name: ['', Validators.required],
        });
        this.courseDescribe = this.fb.group({
            description: ['', Validators.required],
        });
        this.route.params.subscribe(params =>{this.thisCourseId = params['courseId'];});
    }

    updateCourse() {
        const finalData = {...this.courseName.value, ...this.courseDescribe.value};
        // this.courseData = Object.assign({}, this.courseName.value, this.courseDescribe.value)
        console.log(finalData)
        this.ticketService.updateCourse(this.thisCourseId, finalData)
            .subscribe((res) => {
                if (res) {
                    this.courseName.reset();
                    this.courseDescribe.reset();

                }
            });
        this.router.navigate(['../own-courses'])
    }
}
