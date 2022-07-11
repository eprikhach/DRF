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
export class TicketService {
    endpoint: string = 'http://localhost:8000/api';
    headers = new HttpHeaders({'Content-Type': 'application/json'})
    user_list: User[] = []

    constructor(private http: HttpClient, public router: Router, public authService: AuthService,) {
    }

    createTicket(ticket: Course): Observable<any> {
        let api = `${this.endpoint}/courses/create/`
        return this.http.post(api, ticket, {headers: this.headers})
            .pipe(catchError(this.authService.handleError))
        this.router.navigateByUrl('/home')
    }

    getOwnTicket(): Observable<Course[]> {
        let api = `${this.endpoint}/courses/Teacher/`
        return this.http.get<Course[]>(api, {headers: this.headers}).pipe(
            map((res) => {
                console.log(res)
                return res || {};

            }), catchError(this.authService.handleError)
        );
    }

    getTicket(id: string): Observable<Course> {

        let api = `${this.endpoint}/courses/${id}/`
        return this.http.get<Course>(api, {headers: this.headers}).pipe(
            map((res) => {
                console.log(res)
                return res || {};
            }), catchError(this.authService.handleError)
        );
    }

    updateCourse(id:string, ticket: Course): Observable<Course> {
        let api = `${this.endpoint}/courses/${id}/`
        return this.http.put<Course>(api, ticket, {headers: this.headers}).pipe(
            map((res) => {
                console.log(res)
                return res || {};
            }), catchError(this.authService.handleError)
        );

    }
    deleteCourse(id:string): Observable<Course> {
        let api = `${this.endpoint}/courses/${id}/`
        return this.http.delete<Course>(api, {headers: this.headers}).pipe(
            map((res) => {
                console.log(res)
                return res || {};
            }), catchError(this.authService.handleError)
        );
    }
}
