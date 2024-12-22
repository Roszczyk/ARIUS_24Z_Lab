package com.roszczyk.arius_lab5;
import com.roszczyk.arius_lab5.Task;

import android.content.Intent;
import android.os.Bundle;
import android.widget.AdapterView;
import android.widget.ListView;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private List<Task> taskList;
    private TaskAdapter taskAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");

        taskList = new ArrayList<>();
        taskList.add(new Task("Task 1", "Details for Task 1", sdf.parse("2024-12-20"), false));
        taskList.add(new Task("Task 2", "Details for Task 2", sdf.parse("2024-12-20"), true));

        taskAdapter = new TaskAdapter(this, taskList);
        ListView listView = findViewById(R.id.taskListView);
        listView.setAdapter(taskAdapter);

        listView.setOnItemClickListener((AdapterView<?> parent, View view, int position, long id) -> {
            Task selectedTask = taskList.get(position);
            Intent intent = new Intent(MainActivity.this, TaskDetailsActivity.class);
            intent.putExtra("task", selectedTask);
            startActivity(intent);
        });
    }
}
