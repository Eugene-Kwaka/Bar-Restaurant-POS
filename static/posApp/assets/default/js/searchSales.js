const searchField = document.querySelector("#searchField");


// This will hide the search_results table when searching
const tableOutput = document.querySelector(".table-output");
// Hide data table after search
const appTable = document.querySelector(".app-table");
tableOutput.style.display = "none";

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0) {
        console.log("searchValue", searchValue);
    
        fetch("/search-sales", {
            body: JSON.stringify({ searchText: searchValue }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                // After searc_results have been retrieved hide the data table
                appTable.style.display = "none";
                // After search_-results display results table
                tableOutput.style.display = "block";

                if (data.length === 0) {
                    tableOutput.innerHTML = "No results found";
                }
            });
    
    
    }else{
        appTable.style.display = "block";
    }
}
);