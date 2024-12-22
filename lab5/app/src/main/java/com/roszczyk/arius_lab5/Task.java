package com.roszczyk.arius_lab5;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");

public class Task {
    private String title;
    private String details;
    private Date deadline;
    private boolean done;

    public Task(String title, String details, Date deadline, boolean done) {
        this.title = title;
        this.details = details;
        this.deadline = deadline;
        this.done = done; // True - wykonane, False - niewykonane
    }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDetails() { return details; }
    public void setDetails(String details) { this.details = details; }
    public Date getDeadline() { return deadline; }
    public void setDeadline(String deadlineString) {
        this.deadline = deadline;
    }
    public boolean getStatus() { return done; }
    public void setStatus(boolean status) { this.done = status; }
    public boolean isOverdue(){
        return !this.done && this.deadline.before(new Date());
    }
}
