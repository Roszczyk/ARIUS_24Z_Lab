package com.roszczyk.arius_lab5;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.io.Serializable;


public class Task implements Serializable{
    private String title;
    private String details;
    private String deadline;
    private boolean done;

    public Task(String title, String details, String deadline, boolean done) {
        this.title = title;
        this.details = details;
        this.deadline = deadline;
        this.done = done; // True - wykonane, False - niewykonane
    }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDetails() { return details; }
    public void setDetails(String details) { this.details = details; }
    public String getDeadline() { return deadline; }
    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }
    public boolean getStatus() { return done; }
    public void setStatus(boolean status) { this.done = status; }
    public boolean isOverdue(){
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        Date date;
        try {
            date = sdf.parse(this.deadline);
        } catch (ParseException e) {
            System.err.println("Invalid date format: " + this.deadline);
            return false;
        }
        return !this.done && date.before(new Date());
    }
}
