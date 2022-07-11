import {Component, OnInit} from '@angular/core';
import {Course} from "../shared/ticket";
import {TicketService} from "../shared/ticket.service";
import {Observable} from "rxjs";
import {map} from "rxjs/operators";
import {ActivatedRoute, Router} from "@angular/router";
import { AuthService} from "../shared/auth.service";
import { LectureService} from "../shared/lecture.service";
import { Lecture} from "../shared/lecture";

@Component({
    selector: 'app-show-course',
    templateUrl: './show-course.component.html',
    styleUrls: ['./show-course.component.sass']
})
export class ShowCourseComponent implements OnInit {
    thisCourseId!: string;
    lectureList!: Lecture[];
    lecture!: Lecture;

    course_info!: Course


    constructor(public ticketService: TicketService,
                public router: Router,
                private route: ActivatedRoute,
                public authService: AuthService,
                public lectureService: LectureService) {
        this.route.params.subscribe(params => {
            this.thisCourseId = params['courseId'];
        })
        this.lectureService.getCourseLectures(this.thisCourseId).subscribe((res: any) => {

                this.lectureList = res
                console.log(res.value)
            });
    }

    ngOnInit(): void {
        this.route.params.subscribe(params =>{this.thisCourseId = params['courseId'];});
        this.ticketService.getTicket(this.thisCourseId).subscribe((res: any) => {
            this.course_info = res;
        });
    }

    deleteCourse() {
        this.ticketService.deleteCourse(this.thisCourseId).subscribe((res: any) =>{
            console.log(res)
        })
        this.router.navigate([`own-courses`])
        // this.course = this.ticketService.getOwnTicket(id)
    }

    updCourse(id: string){
        this.router.navigate([`course-upd/${id}`])
    }

    createLecture(id:string){
        this.router.navigate([`${id}/create-lecture`])
    }

    // createCourse() {
    //       const finalData = {...this.courseName.value, ...this.courseDescribe.value};
    //       // this.courseData = Object.assign({}, this.courseName.value, this.courseDescribe.value)
    //       console.log(finalData)
    //       this.ticketService.createTicket(finalData)
    //           .subscribe((res) => {
    //           if (res.result) {
    //               this.courseName.reset();
    //               this.courseDescribe.reset();
    //
    //           }
    //       });
    //       this.router.navigate(['../home'])
    //   }

}
