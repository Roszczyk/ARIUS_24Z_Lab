package com.roszczyk.arius_lab5;

import .Task;

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

        // Inicjalizacja widoków
        titleTextView = findViewById(R.id.taskDetailsTitle);
        descriptionTextView = findViewById(R.id.taskDetailsDescription);
        deadlineTextView = findViewById(R.id.taskDetailsDeadline);
        statusTextView = findViewById(R.id.taskDetailsStatus);
        completeButton = findViewById(R.id.completeButton);
        pendingButton = findViewById(R.id.pendingButton);

        // Pobieranie danych z intencji
        Intent intent = getIntent();
        Task task = (Task) intent.getSerializableExtra("task");

        if (task != null) {
            // Ustawianie szczegółów zadania
            titleTextView.setText(task.getTitle());
            descriptionTextView.setText(task.getDescription());
            deadlineTextView.setText(task.getDeadline());
            statusTextView.setText(task.getStatus());
        }

        // Obsługa przycisku "Zakończ"
        completeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (task != null) {
                    task.setStatus("completed");
                    statusTextView.setText("completed");
                }
            }
        });

        // Obsługa przycisku "W toku"
        pendingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (task != null) {
                    task.setStatus("pending");
                    statusTextView.setText("pending");
                }
            }
        });
    }
}