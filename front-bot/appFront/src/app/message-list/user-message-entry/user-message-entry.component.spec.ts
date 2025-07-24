import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserMessageEntryComponent } from './user-message-entry.component';

describe('UserMessageEntryComponent', () => {
  let component: UserMessageEntryComponent;
  let fixture: ComponentFixture<UserMessageEntryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserMessageEntryComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UserMessageEntryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
