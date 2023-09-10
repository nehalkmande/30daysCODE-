// JavaScript
function addTask() {
    const taskInput = document.getElementById('task');
    const taskText = taskInput.value.trim();
    
    if (taskText !== '') {
        const taskList = document.getElementById('task-list');
        const taskItem = document.createElement('li');
        
        taskItem.innerHTML = `
            <input type="checkbox">
            <span>${taskText}</span>
            <button onclick="deleteTask(this)">Delete</button>
        `;
        
        taskList.appendChild(taskItem);
        taskInput.value = '';
    }
}

function deleteTask(button) {
    const taskList = document.getElementById('task-list');
    const taskItem = button.parentElement;
    taskList.removeChild(taskItem);
}
