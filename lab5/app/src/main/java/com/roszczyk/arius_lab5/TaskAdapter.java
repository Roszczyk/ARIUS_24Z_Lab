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
        View itemView = convertView;
        if (itemView == null) {
            itemView = LayoutInflater.from(getContext()).inflate(R.layout.task_item, parent, false);
        }

        Task currentTask = getItem(position);

        TextView titleTextView = itemView.findViewById(R.id.taskTitle);
        titleTextView.setText(currentTask.getTitle());

        TextView deadlineTextView = itemView.findViewById(R.id.taskDeadline);
        deadlineTextView.setText(currentTask.getDeadline());

        ImageView statusIcon = itemView.findViewById(R.id.taskStatusIcon);
        if (currentTask.getStatus()) {
            statusIcon.setImageResource(R.drawable.ic_completed);
        } else if (currentTask.isOverdue()) {
            statusIcon.setImageResource(R.drawable.ic_overdue);
        } else {
            statusIcon.setImageResource(R.drawable.ic_pending);
        }

        return itemView;
    }
}
