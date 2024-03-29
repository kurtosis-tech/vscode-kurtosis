"use strict";
/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// import net = require("net")
const child_process_1 = require("child_process");
const vscode_1 = require("vscode");
const node_1 = require("vscode-languageclient/node");
let client;
function activate(context) {
    // Options to control the language client
    const clientOptions = {
        // Register the server for plain text documents
        documentSelector: [{ scheme: 'file', language: 'starlark' }],
        synchronize: {
            // Notify the server about file changes to '.clientrc files contained in the workspace
            fileEvents: vscode_1.workspace.createFileSystemWatcher('**.star')
        }
    };
    // Create the language client and start the client
    client = new node_1.LanguageClient("klsp", 'klsp', () => startServer(), clientOptions);
    // Start the client. This will also launch the server
    client.start();
}
exports.activate = activate;
function deactivate() {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
exports.deactivate = deactivate;
async function startServer() {
    // const socket = net.connect({ host: "127.0.0.1", port:8484})
    // return { writer: socket, reader: socket }
    return (0, child_process_1.spawn)("kurtosis", ["lsp", "start"]);
}
//# sourceMappingURL=extension.js.map