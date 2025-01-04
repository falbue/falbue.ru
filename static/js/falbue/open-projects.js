fetch('/api/projects')
.then(response => response.json())
.then(projects => {
    const container = document.getElementById('projects-container');
    projects.forEach(project => {
                    // Создаем карточку для каждого проекта
        const card = document.createElement('div');
        card.classList.add('card');

                    // Создаем элементы карточки
        const header = document.createElement('header');
        const name = document.createElement('h3');
        name.textContent = project.name;
        header.appendChild(name);

        const main = document.createElement('main');
        const about = document.createElement('h4');
        about.textContent = project.about;
        main.appendChild(about);

        const footer = document.createElement('footer');
        const githubLink = document.createElement('a');
        footer.appendChild(githubLink);
        fetch(`/static/icons/github.svg`)
        .then(response => response.text())
        .then(svgText => {
            githubLink.href = project.url;
            githubLink.innerHTML = svgText;
            githubLink.classList.add('h3');
        });


        const homepageLink = document.createElement('a');
        homepageLink.href = project.homepage;
        const openText = document.createElement('h4');
        openText.textContent = 'открыть ›';
        homepageLink.appendChild(openText);
        footer.appendChild(homepageLink);

                    // Собираем карточку
        card.appendChild(header);
        card.appendChild(main);
        card.appendChild(footer);

                    // Вставляем карточку в контейнер
        container.appendChild(card);
    });
})
.catch(error => {
    console.error('Ошибка при загрузке данных:', error);
});