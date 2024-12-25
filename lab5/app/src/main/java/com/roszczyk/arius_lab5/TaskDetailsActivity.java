package com.roszczyk.arius_lab5;

import com.roszczyk.arius_lab5.Task;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.view.MenuItem;

import androidx.appcompat.app.AppCompatActivity;

public class TaskDetailsActivity extends AppCompatActivity {

    private TextView titleTextView;
    private TextView descriptionTextView;
    private TextView deadlineTextView;
    private TextView statusTextView;
    private Button completeButton;
    private Button pendingButton;
    private Task task;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_task_details);

        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }

        titleTextView = findViewById(R.id.taskDetailsTitle);
        descriptionTextView = findViewById(R.id.taskDetailsDescription);
        deadlineTextView = findViewById(R.id.taskDetailsDeadline);
        statusTextView = findViewById(R.id.taskDetailsStatus);
        completeButton = findViewById(R.id.completeButton);
        pendingButton = findViewById(R.id.pendingButton);

        Intent intent = getIntent();
        task = (Task) intent.getSerializableExtra("task");

        if (task != null) {
            titleTextView.setText(task.getTitle());
            descriptionTextView.setText(task.getDetails());
            deadlineTextView.setText(task.getDeadline());
            updateStatusText(task);
        }

        completeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (task != null) {
                    task.setStatus(true);
                    updateStatusText(task);
                }
            }
        });

        pendingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (task != null) {
                    task.setStatus(false);
                    updateStatusText(task);
                }
            }
        });
    }

    private void updateStatusText(Task task) {
        if (task.getStatus()) {
            statusTextView.setText("completed");
        } else if (task.isOverdue()) {
            statusTextView.setText("overdue");
        } else {
            statusTextView.setText("pending");
        }
    }

    // Obsługa strzałki powrotu
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (item.getItemId() == android.R.id.home) {
            Intent resultIntent = new Intent();
            resultIntent.putExtra("updatedTask", task);
            setResult(RESULT_OK, resultIntent);
            finish();
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onPause() {
        super.onPause();
        Intent resultIntent = new Intent();
        resultIntent.putExtra("updatedTask", task);
        setResult(RESULT_OK, resultIntent);
    }
}
