import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {Router} from '@angular/router';
import { TicketService} from "../shared/ticket.service";
import {UserService} from "../shared/user.service";
import {debounceTime, distinctUntilChanged, Observable, Subject, switchMap} from "rxjs";
import {User} from "../shared/user";

@Component({
  selector: 'app-create-course',
  templateUrl: './create-course.component.html',
  styleUrls: ['./create-course.component.sass']
})
export class CreateCourseComponent implements OnInit {users$!: Observable<User[]>
    private searchTerms = new Subject<string>()
    ticketForm: FormGroup;



    constructor(
        public fb: FormBuilder,
        public router: Router,
        public ticketService: TicketService,
        private userService: UserService
    ) {
        this.ticketForm = this.fb.group({
            subject: [''],
            ticket_status: [''],
            description: [''],
            supports: ['']
        });
    }

    ngOnInit() {
    this.users$ = this.searchTerms.pipe(
      // wait 300ms after each keystroke before considering the term
      debounceTime(300),

      // ignore new term if same as previous term
      distinctUntilChanged(),

      // switch to new search observable each time the term changes
      switchMap((term: string) => this.userService.searchUsers(term)),
    );
  }
    search(term: string): void {
    this.searchTerms.next(term);
  }

    createTicket() {
        this.ticketForm.value.supports = this.ticketForm.value.supports.split(',')
        this.ticketService.createTicket(this.ticketForm.value).subscribe((res)=>{
            if (res.result){
                console.log('okay')
            }
        })
    }



}

