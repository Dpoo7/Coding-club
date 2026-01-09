function generateCard() {
    document.getElementById("cname").textContent =
        document.getElementById("name").value || "---";

    document.getElementById("csid").textContent =
        document.getElementById("sid").value || "---";

    document.getElementById("cclass").textContent =
        document.getElementById("class").value || "---";

    document.getElementById("cschool").textContent =
        document.getElementById("school").value || "---";
}
