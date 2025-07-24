import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AssistantMessageEntryComponent } from './assistant-message-entry.component';

describe('AssistantMessageEntryComponent', () => {
  let component: AssistantMessageEntryComponent;
  let fixture: ComponentFixture<AssistantMessageEntryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AssistantMessageEntryComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AssistantMessageEntryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
