import json
import os

# =====================================================
# CREAR JSON SI NO EXISTE
# =====================================================

if not os.path.exists("plays.json"):

    with open("plays.json", "w") as file:
        json.dump([], file)

# =====================================================
# CARGAR PLAYS
# =====================================================

with open("plays.json", "r") as file:

    contenido = file.read()

    if contenido.strip() == "":
        plays = []
    else:
        plays = json.loads(contenido)

# =====================================================
# CREAR NUEVA PLAY
# =====================================================

crear = input(
    "Do you want to create a new play? (y/n): "
)

if crear.lower() == "y":

    play = input("Play Name: ")

    playclock = int(
        input("Segments Amount: ")
    )

    strength = input("Strength: ")

    weakness = input("Weakness: ")

    description = input("Description: ")

    complete_play = {

        "Name": play,
        "Segments": playclock,
        "Strength": strength,
        "Weakness": weakness,
        "Description": description

    }

    # AGREGAR AL FINAL

    plays.append(complete_play)

    # GUARDAR JSON

    with open("plays.json", "w") as file:

        json.dump(plays, file, indent=4)

    print("Play Saved.")

# =====================================================
# GENERAR HTML
# =====================================================

html = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<title>Play Creator</title>

<style>

body {

    background-color: #1e1e1e;
    color: white;
    font-family: Arial;
    padding: 30px;
}

h1 {

    text-align: center;
    color: crimson;
}

.main-btn {

    background-color: crimson;
    color: white;
    border: none;
    padding: 12px 18px;
    border-radius: 10px;
    cursor: pointer;
    margin-bottom: 30px;
    transition: 0.3s;
}

.main-btn:hover {

    transform: scale(1.05);
}

#creatorMenu {

    display: none;
    background-color: #2d2d2d;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.play-card {

    background-color: #2d2d2d;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.segment-container {

    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.segment {

    width: 40px;
    height: 40px;
    border-radius: 8px;
    background-color: #555;
    transition: 0.3s;
}

.filled {

    background-color: limegreen;
}

.info {

    display: none;
    margin-top: 15px;
}

.card-btn {

    background-color: crimson;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 10px;
    cursor: pointer;
    margin-right: 10px;
    margin-top: 10px;
}

</style>

</head>

<body>

<h1>Play Creator</h1>

<button
    class="main-btn"
    onclick="toggleCreator()"
>
    Create New Play
</button>

<div id="creatorMenu">

    <p>

        To create a new play:

    </p>

    <ol>

        <li>
            Close this page
        </li>

        <li>
            Run main.py again
        </li>

        <li>
            Type "y"
        </li>

    </ol>

</div>
"""

# =====================================================
# AGREGAR LAS PLAYS
# =====================================================

for play in plays:

    segments_html = ""

    for i in range(play["Segments"]):

        segments_html += """
        <div class="segment"></div>
        """

    html += f"""

    <div class="play-card">

        <h2>{play["Name"]}</h2>

        <div class="segment-container">

            {segments_html}

        </div>

        <button
            class="card-btn"
            onclick="toggleInfo(this)"
        >
            Show / Hide Info
        </button>

        <button
            class="card-btn"
            onclick="fillSegment(this)"
        >
            Fill Segment
        </button>

        <button
            class="card-btn"
            onclick="removeSegment(this)"
        >
            Remove Segment
        </button>

        <div class="info">

            <p>

                <strong>Strength:</strong>

                {play["Strength"]}

            </p>

            <p>

                <strong>Weakness:</strong>

                {play["Weakness"]}

            </p>

            <p>

                <strong>Description:</strong>

                {play["Description"]}

            </p>

        </div>

    </div>
    """

# =====================================================
# JAVASCRIPT
# =====================================================

html += """

<script>

function toggleCreator() {

    let menu =
        document.getElementById("creatorMenu");

    if (menu.style.display === "none") {

        menu.style.display = "block";

    } else {

        menu.style.display = "none";
    }
}

function toggleInfo(button) {

    let info =
        button.parentElement.querySelector(".info");

    if (info.style.display === "block") {

        info.style.display = "none";

    } else {

        info.style.display = "block";
    }
}

function fillSegment(button) {

    let card =
        button.parentElement;

    let segments =
        card.querySelectorAll(".segment");

    for (let i = 0; i < segments.length; i++) {

        if (
            !segments[i]
            .classList
            .contains("filled")
        ) {

            segments[i]
                .classList
                .add("filled");

            break;
        }
    }
}

function removeSegment(button) {

    let card =
        button.parentElement;

    let segments =
        card.querySelectorAll(".segment");

    for (
        let i = segments.length - 1;
        i >= 0;
        i--
    ) {

        if (
            segments[i]
            .classList
            .contains("filled")
        ) {

            segments[i]
                .classList
                .remove("filled");

            break;
        }
    }
}

</script>

</body>
</html>
"""

# =====================================================
# GUARDAR HTML
# =====================================================

with open(
    "index.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(html)

# =====================================================
# ABRIR AUTOMATICAMENTE
# =====================================================

linux_path = os.path.abspath("index.html")

windows_path = os.popen(
    f'wslpath -w "{linux_path}"'
).read().strip()

os.system(
    f'cmd.exe /c start "" "{windows_path}"'
)

print("Project generated correctly.")