package com.roszczyk.arius_lab5;

import android.content.Intent;
import android.os.Bundle;
import android.widget.AdapterView;
import android.widget.ListView;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private List<Task> taskList;
    private TaskAdapter taskAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        taskList = new ArrayList<>();
        taskList.add(new Task("Task 1", "Details for Task 1", "2024-12-20", false));
        taskList.add(new Task("Task 2", "Details for Task 2", "2024-12-20", true));
        taskList.add(new Task("Task 3", "Details for Task 3", "2024-12-30", false));
        taskList.add(new Task("Task 4", "Details for Task 4", "2024-12-30", true));

        taskAdapter = new TaskAdapter(this, taskList);
        ListView listView = findViewById(R.id.taskListView);
        listView.setAdapter(taskAdapter);

        listView.setOnItemClickListener((AdapterView<?> parent, View view, int position, long id) -> {
            Task selectedTask = taskList.get(position);
            Intent intent = new Intent(MainActivity.this, TaskDetailsActivity.class);
            intent.putExtra("task", selectedTask);
            startActivityForResult(intent, 1);
        });
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 1 && resultCode == RESULT_OK) {
            Task updatedTask = (Task) data.getSerializableExtra("updatedTask");
            if (updatedTask != null) {
                for (int i = 0; i < taskList.size(); i++) {
                    if (taskList.get(i).getTitle().equals(updatedTask.getTitle())) {
                        taskList.set(i, updatedTask);
                        break;
                    }
                }
                taskAdapter.notifyDataSetChanged();
            }
        }
    }
}
