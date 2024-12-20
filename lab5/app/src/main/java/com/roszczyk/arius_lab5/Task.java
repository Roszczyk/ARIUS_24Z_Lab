package com.roszczyk.arius_lab5;

public class Task {
    private String title;
    private String details;
    private String deadline;
    private String status;

    public Task(String title, String details, String deadline, String status) {
        this.title = title;
        this.details = details;
        this.deadline = deadline;
        this.status = status;
    }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDetails() { return details; }
    public void setDetails(String details) { this.details = details; }
    public String getDeadline() { return deadline; }
    public void setDeadline(String deadline) { this.deadline = deadline; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}