from pathlib import Path
import matplotlib.pyplot as plt

ROOT_DIR = Path(__file__).resolve().parents[1]
ENVS = ["internal-devnet", "devnet", "testnet"]

def count_rollapps(base: Path) -> int:
    count = 0
    for item in base.iterdir():
        if item.is_dir() and any(child.suffix == '.json' for child in item.glob('*.json')):
            count += 1
    return count

def main():
    counts = {}
    for env in ENVS:
        path = ROOT_DIR / env
        if path.is_dir():
            counts[env] = count_rollapps(path)
    if not counts:
        print('No environments found.')
        return

    plt.figure(figsize=(8, 4))
    plt.bar(counts.keys(), counts.values(), color='skyblue')
    plt.title('RollApps Count per Environment')
    plt.ylabel('Number of RollApps')
    for i, v in enumerate(counts.values()):
        plt.text(i, v + max(counts.values()) * 0.01, str(v), ha='center')
    output_path = ROOT_DIR / 'rollapps_count.png'
    plt.tight_layout()
    plt.savefig(output_path)
    print(f'Saved bar chart to {output_path}')

if __name__ == '__main__':
    main()
