package com.roszczyk.arius_lab5;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;

public class TaskAdapter extends ArrayAdapter<Task> {
    public TaskAdapter(Context context, List<Task> tasks) {
        super(context, 0, tasks);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.task_item, parent, false);
        }

        Task task = getItem(position);

        TextView taskTitle = convertView.findViewById(R.id.taskTitle);
        TextView taskDeadline = convertView.findViewById(R.id.taskDeadline);
        ImageView taskStatusIcon = convertView.findViewById(R.id.taskStatusIcon);

        taskTitle.setText(task.getTitle());
        taskDeadline.setText(task.getDeadline());

        int iconRes = task.getStatus() ?
                android.R.drawable.presence_online :
                android.R.drawable.presence_offline;
        taskStatusIcon.setImageResource(iconRes);

        return convertView;
    }
}
