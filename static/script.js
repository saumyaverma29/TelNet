// Fetch and display projects dynamically
window.onload = function() {
    fetch('/api/projects')
        .then(response => response.json())
        .then(data => {
            const projectList = document.getElementById('project-list');
            data.projects.forEach(project => {
                const projectElement = document.createElement('div');
                projectElement.classList.add('project');
                projectElement.innerHTML = `
                    <h3>${project.title}</h3>
                    <p>${project.description}</p>
                    <p><strong>Budget:</strong> $${project.budget}</p>
                `;
                projectList.appendChild(projectElement);
            });
        })
        .catch(error => console.error('Error fetching projects:', error));
};

