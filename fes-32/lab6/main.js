let page = 1;


function add_data(data) {
    let main = document.getElementById('main')
    let data_list = data.data

    data_list.forEach(element => {
        let p = document.createElement('p')
        p.textContent = element.fact;
        main.appendChild(p)
    });
}

function fetchDatabyfetch() {
    fetch(`https://catfact.ninja/facts?page=${page}`)
        .then(response => {
            return response.json();
        })
        .then(data => {
            add_data(data);

            page++;
            setTimeout(fetchDatabyfetch, 1000);


        })
        .catch(error => {
            console.error(error)
        });
}

async function fetchDatabyasync() {
    try {

        let response = await fetch(`https://catfact.ninja/facts?page=${page}`);
        let data = await response.json();

        add_data(data);
        page++;
        setTimeout(fetchDatabyasync, 1000);
    } catch (error) {
        console.error(error)
    }

}


function fetchDatabyXHR() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `https://catfact.ninja/facts?page=${page}`, true)

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let data = JSON.parse(xhr.responseText)


            add_data(data)
            page++;
            setTimeout(fetchDatabyXHR, 1000)

        }
    }
    xhr.send()

}


fetchDatabyfetch();
// fetchDatabyasync();
// fetchDatabyXHR();