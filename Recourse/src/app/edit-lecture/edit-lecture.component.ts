import { Component, OnInit } from '@angular/core';
import {Lecture} from "../shared/lecture";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../shared/auth.service";
import {ActivatedRoute, Router} from "@angular/router";
import {LectureService} from "../shared/lecture.service";
import {UserService} from "../shared/user.service";

@Component({
  selector: 'app-edit-lecture',
  templateUrl: './edit-lecture.component.html',
  styleUrls: ['./edit-lecture.component.sass']
})

export class EditLectureComponent implements OnInit {
lecture!: Lecture
    lectureName!: FormGroup;
    lectureFile!: FormGroup;
    thisCourseId!: string;
    thisLectureId!: string;
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

        this.route.params.subscribe(params => {
            this.thisLectureId = params['lectureId'];
        })
    }

    onFileSelected(event: any) {
        const file: File = event.target.files[0];
        console.log(file)

        if (file) {

            this.fileName = file.name;

            this.formData.append("presentation", file);
            this.formData.append('theme', this.lectureName.value.theme);


        }
    }

    editLecture() {
        this.lectureService.editLecture(this.thisCourseId, this.thisLectureId, this.formData)
            .subscribe((res) => {
                if (res) {
                    console.log(res)
                }
            });

    }
}
