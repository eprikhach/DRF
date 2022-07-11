import {Component, OnInit} from '@angular/core';
import {Lecture} from "../shared/lecture";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../shared/auth.service";
import {ActivatedRoute, Router} from "@angular/router";
import {TicketService} from "../shared/ticket.service";
import {UserService} from "../shared/user.service";
import {LectureService} from "../shared/lecture.service";


@Component({
    selector: 'app-create-lecture',
    templateUrl: './create-lecture.component.html',
    styleUrls: ['./create-lecture.component.sass']
})
export class CreateLectureComponent implements OnInit {
    lecture!: Lecture
    lectureName!: FormGroup;
    lectureFile!: FormGroup;
    thisCourseId!: string;
    fileName = '';
    formData = new FormData();

    // formData = new FormData();


    constructor(public authService: AuthService,
                public fb: FormBuilder,
                public router: Router,
                public lectureService: LectureService,
                private userService: UserService,
                private route: ActivatedRoute,) {

    }


    ngOnInit(): void {
        this.lectureName = this.fb.group({
            theme: ['', Validators.required],
        });
        this.lectureFile = this.fb.group({
            presentation: ['', Validators.required],
        });

        this.route.params.subscribe(params => {
            this.thisCourseId = params['courseId'];
        })
    }

    onFileSelected(event: any) {
        const file: File = event.target.files[0];
        console.log(file)

        if (file) {

            this.fileName = file.name;

            this.formData.append("presentation", file);
            this.formData.append('theme', this.lectureName.value.theme);


            this.lectureService.createLecture(this.thisCourseId, this.formData)
            console.log(this.formData)

        }
    }

    createLecture() {
        const finalData = {...this.lectureName.value, ...this.lectureFile.value};
        // this.courseData = Object.assign({}, this.courseName.value, this.courseDescribe.value)
        for (const entry of this.formData.entries()) {
                console.log(entry)
            }
        this.lectureService.createLecture(this.thisCourseId, this.formData)
            .subscribe((res) => {
                if (res) {
                    console.log(res)
                }
            });

    }
}
