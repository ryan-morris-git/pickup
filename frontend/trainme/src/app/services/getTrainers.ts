export default async function getTrainers() {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const response = await fetch("http://127.0.0.1:8000/api/get_training", {
        method: "POST",
        body: JSON.stringify({}),
        headers: myHeaders
    });

    return await response.json()
}