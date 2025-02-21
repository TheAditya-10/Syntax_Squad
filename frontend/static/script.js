const fetchPlaces = async () => {
    let days = document.getElementById("days").value;
    let mood = document.getElementById("mood").value;
    let budget = document.getElementById("budget").value;

    if (!days || !mood || !budget) {
        alert("Please fill all fields!");
        return;
    }
    console.log("Sending request to /planner...");

    let response = await fetch("/planner", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ days, mood, budget }),
    });

    console.log("Received response:", response);
    let data = await response.json();
    let placeList = document.getElementById("placeList");
    placeList.innerHTML = ""; // Clear previous results

    if (data.suggested_places) {
        document.getElementById("destinations").classList.remove("hidden");

        data.suggested_places.split("\n").forEach((place) => {
            let button = document.createElement("button");
            button.innerText = place;
            button.className = "block bg-yellow-500 text-white p-2 rounded mt-2 hover:bg-yellow-700 transition";
            button.onclick = () => generateTripPlan(place);
            placeList.appendChild(button);
        });
    } else {
        alert("No places found! Try again.");
    }
};

const generateTripPlan = async (selected_place) => {
    let response = await fetch("/generate_trip_plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selected_place }),
    });

    let data = await response.json();
    document.getElementById("itinerary").innerText = data.trip_plan;
    document.getElementById("itinerarySection").classList.remove("hidden");
    document.getElementById("confirmTripSection").classList.remove("hidden");
};

const confirmTrip = async () => {
    let email = document.getElementById("email").value;
    let start_date = document.getElementById("startDate").value;
    let end_date = document.getElementById("endDate").value;
    let place_visited = document.getElementById("itinerary").innerText.split("\n")[0]; // First line of itinerary
    let budget_per_person = document.getElementById("budget").value;
    let companions = document.getElementById("companions").value;

    if (!email || !start_date || !end_date || !place_visited || !budget_per_person) {
        alert("Please fill all required fields!");
        return;
    }

    let response = await fetch("/confirm_trip", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, start_date, end_date, place_visited, budget_per_person, companions }),
    });

    let data = await response.json();
    alert(data.message || "Trip confirmed successfully!");
};
