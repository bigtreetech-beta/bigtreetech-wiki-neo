import { spawnSync } from "child_process";
import fs from "fs";
import path from "path";

const isWin = process.platform === "win32";

const venvPath = ".venv";
const lockFile = ".venv/.installed";

const venvPython = isWin
    ? path.join(venvPath, "Scripts", "python.exe")
    : path.join(venvPath, "bin", "python");

function run(cmd: string, args: string[]) {
    const res = spawnSync(cmd, args, { stdio: "inherit" });
    if (res.status !== 0) process.exit(res.status ?? 1);
}

function ensureLockDir() {
    const dir = path.dirname(lockFile);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
}

function main() {
    console.log("🚀 setup venv");

    // check lockfile
    if (fs.existsSync(lockFile)) {
        console.log("lock file exists, skip setup");
        return;
    }

    if (!fs.existsSync(venvPython)) {
        console.log("📦 creating venv...");
        run(isWin ? "python" : "python3", ["-m", "venv", venvPath]);
    } else {
        console.log("✅ venv exists");
    }

    console.log("upgrading pip...");
    run(venvPython, ["-m", "pip", "install", "--upgrade", "pip"]);

    const req = path.join("script", "requirements.txt");

    if (fs.existsSync(req)) {
        console.log("📦 installing requirements...");
        run(venvPython, ["-m", "pip", "install", "-r", req]);
    } else {
        console.log("❗ no requirements.txt");
    }

    // make lockfile
    ensureLockDir();
    fs.writeFileSync(lockFile, "installed");

    console.log("✅ done");
}

main();
