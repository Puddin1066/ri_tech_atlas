import { cpSync, existsSync, mkdirSync, rmSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const atlasRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const src = path.join(atlasRoot, "../../data");
const dest = path.join(atlasRoot, "data");

if (!existsSync(src)) {
  console.warn(`sync-data: source missing (${src}); skipping`);
  process.exit(0);
}

rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
cpSync(src, dest, { recursive: true });
console.log(`sync-data: copied ${src} → ${dest}`);
