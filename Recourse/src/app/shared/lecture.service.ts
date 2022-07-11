import {Lecture} from "./lecture";
import {Injectable} from '@angular/core';
import {Course} from './ticket';
import {Observable, throwError} from 'rxjs';
import {catchError, map} from 'rxjs/operators';
import {
    HttpClient,
    HttpHeaders,
    HttpErrorResponse,
} from '@angular/common/http';
import {Router} from '@angular/router';
import {AuthService} from "./auth.service";
import {User} from "./user";

@Injectable({
    providedIn: 'root'
})
export class LectureService {
    endpoint: string = 'http://localhost:8000/api';
    headers = new HttpHeaders({'Content-Type': 'form-data', 'Accept': 'application/json'})

    constructor(private http: HttpClient, public router: Router, public authService: AuthService) {
    }

    createLecture(course_id: string, lecture: FormData): Observable<any> {
        let api = `${this.endpoint}/courses/${course_id}/lectures/create/`
        return this.http.post(api, lecture)
            .pipe(catchError(this.authService.handleError))
        this.router.navigateByUrl('/home')
    }

    editLecture(course_id:string, lecture_id: string, lecture: FormData): Observable<any>{
        let api = `${this.endpoint}/courses/${course_id}/lectures/${lecture_id}/`
        return this.http.put(api, lecture)
            .pipe(catchError(this.authService.handleError))
        this.router.navigate([`course/${course_id}`])
    }

    getCourseLectures(course_id: string): Observable<Lecture[]> {
        let api = `${this.endpoint}/courses/${course_id}/course_lectures/`
        return this.http.get<Lecture[]>(api, {headers: this.headers}).pipe(
            map((res) => {
                console.log(res)
                return res || {};

            }), catchError(this.authService.handleError)
        );
    }
}
