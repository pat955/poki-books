import toml
import subprocess
import re

def get_latest_git_tag():
    try:
        tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).strip().decode('utf-8')
        return tag
    except subprocess.CalledProcessError:
        return None

def update_pyproject_version(tag):
    pyproject_file = 'pyproject.toml'
    with open(pyproject_file, 'r') as file:
        pyproject_data = toml.load(file)

    pyproject_data['tool']['poetry']['version'] = tag.lstrip('v')

    with open(pyproject_file, 'w') as file:
        toml.dump(pyproject_data, file)

def update_setup_version(tag):
    setup_file = 'setup.py'
    version_pattern = re.compile(r'version\s*=\s*[\'"]([^\'"]*)[\'"]')
    
    with open(setup_file, 'r') as file:
        setup_content = file.read()

    new_setup_content = version_pattern.sub(f"version='{tag.lstrip('v')}'", setup_content)
    
    with open(setup_file, 'w') as file:
        file.write(new_setup_content)

if __name__ == "__main__":
    latest_tag = get_latest_git_tag()
    if latest_tag:
        update_pyproject_version(latest_tag)
        update_setup_version(latest_tag)
    else:
        print("No git tags found.")