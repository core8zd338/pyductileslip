"""sampler_eaad2a - Environment inspector."""
import platform, os, json
LABEL = "sampler_eaad2a"
def collect_info() -> dict:
    return {"label": LABEL, "python": platform.python_version(), "os": platform.system(), "arch": platform.machine(), "cwd": os.getcwd(), "user": os.getenv("USER", "unknown")}
def main():
    info = collect_info()
    print(json.dumps(info, indent=2))
if __name__ == "__main__":
    main()
