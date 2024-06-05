const vscode = require('vscode');

function activate(context) {
    let disposable = vscode.commands.registerCommand('my-extension.addFire', function () {
        let editor = vscode.window.activeTextEditor;
        if (editor) {
            let document = editor.document;
            let allLines = document.getText().split(/\r?\n/g);

            editor.edit(editBuilder => {
                allLines.forEach((line, i) => {
                    if (line.length >= 50) {
                        let position = new vscode.Position(i, line.length);
                        editBuilder.insert(position, ' 🔥');
                    }
                });
            });
        }
    });

    context.subscriptions.push(disposable);
}

exports.activate = activate;