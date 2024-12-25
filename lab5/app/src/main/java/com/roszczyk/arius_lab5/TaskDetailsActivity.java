package com.roszczyk.arius_lab5;

import com.roszczyk.arius_lab5.Task;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class TaskDetailsActivity extends AppCompatActivity {

    private TextView titleTextView;
    private TextView descriptionTextView;
    private TextView deadlineTextView;
    private TextView statusTextView;
    private Button completeButton;
    private Button pendingButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_task_details);

        titleTextView = findViewById(R.id.taskDetailsTitle);
        descriptionTextView = findViewById(R.id.taskDetailsDescription);
        deadlineTextView = findViewById(R.id.taskDetailsDeadline);
        statusTextView = findViewById(R.id.taskDetailsStatus);
        completeButton = findViewById(R.id.completeButton);
        pendingButton = findViewById(R.id.pendingButton);

        Intent intent = getIntent();
        Task task = (Task) intent.getSerializableExtra("task");

        if (task != null) {
            titleTextView.setText(task.getTitle());
            descriptionTextView.setText(task.getDetails());
            deadlineTextView.setText(task.getDeadline());
            if (task.getStatus()) statusTextView.setText("completed");
            else if (task.isOverdue()) statusTextView.setText("overdue");
            else statusTextView.setText("pending");
        }

        completeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (task != null) {
                    task.setStatus(true);
                    statusTextView.setText("completed");
                }
            }
        });

        pendingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (task != null) {
                    task.setStatus(false);
                    statusTextView.setText("pending");
                }
            }
        });
    }
}