import {Injectable} from '@angular/core';
import {Ticket} from './ticket';
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

    createTicket(ticket: Ticket): Observable<any> {
        let api = `${this.endpoint}/ticket/create/`
        return this.http.post(api, ticket, {headers: this.headers})
            .pipe(catchError(this.authService.handleError))
    }

    createDiv(user: User): void {
        this.user_list.push(user);
    }
}
