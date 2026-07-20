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
const middleware = spawn(venvPython, ["script/build_file_middleware.py", ...args], {
    stdio: "inherit",
});

middleware.on("error", (err: Error) => {
    console.error("Failed to start python process:", err);
});

middleware.on("close", (code: number) => {
    if (code !== 0) {
        process.exit(code ?? 1);
    }

    const build_i18n = spawn(venvPython, ["script/build_file_i18n.py", ...args], {
        stdio: "inherit",
    });

    build_i18n.on("error", (err: Error) => {
        console.error("Failed to start python process:", err);
    });

    build_i18n.on("close", (code: number) => {
        process.exit(code ?? 0);
    });
});
