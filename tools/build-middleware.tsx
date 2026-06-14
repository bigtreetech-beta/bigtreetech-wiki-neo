import { spawn } from "child_process";
import path from "path";
import fs from "fs";

// check system
const isWin: boolean = process.platform === "win32";

// venv python path
const venvPython: string = isWin
    ? path.join(".venv", "Scripts", "python.exe")
    : path.join(".venv", "bin", "python");

// check venv
if (!fs.existsSync(venvPython)) {
    throw new Error(`venv python not found: ${venvPython}`);
}

const args: string[] = process.argv.slice(2);

// run python
const py = spawn(venvPython, ["script/build_file_middleware.py", ...args], {
    stdio: "inherit",
});

// error
py.on("error", (err: Error) => {
    console.error("Failed to start python process:", err);
});
