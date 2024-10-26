import os


def generate_markdown_structure(root_dir, skip_folders, indent=''):
    """Recursively generates a markdown representation of the directory structure with icons."""
    markdown_structure = ''
    items = sorted(os.listdir(root_dir))

    for index, item in enumerate(items):
        if item in skip_folders:
            continue

        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            icon = '🗂️'
            connector = '└── ' if index == len(items) - 1 else '├── '
            markdown_structure += f"{indent}{connector}{icon} {item}\n"
            sub_indent = indent + ('    ' if connector == '└── ' else '│   ')
            markdown_structure += generate_markdown_structure(path, skip_folders, sub_indent)
        else:
            icon = '📄'
            connector = '└── ' if index == len(items) - 1 else '├── '
            markdown_structure += f"{indent}{connector}{icon} {item}\n"

    return markdown_structure


folder_path = '/Users/samarthgoudar/Documents' 
skip_folders = ['_drafts', '_includes', 'node_modules' , '.git']

markdown_output = generate_markdown_structure(folder_path, skip_folders)

with open('project_structure.md', 'w') as f:
    f.write(markdown_output)

print("Markdown structure saved to 'project_structure.md'.")
