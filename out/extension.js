"use strict";
/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const child_process_1 = require("child_process");
const path = require("path");
const vscode_1 = require("vscode");
const node_1 = require("vscode-languageclient/node");
let client;
function activate(context) {
    // The server is implemented in node
    const file = context.asAbsolutePath(path.join('execute.sh'));
    // const logFile = context.asAbsolutePath(
    // 	path.join('debugger.txt')
    // );
    // If the extension is launched in debug mode then the debug server options are used
    // Otherwise the run options are used
    const serverOptions = {
        run: { command: "bash", args: [file] },
        debug: { command: "bash", args: [file] }
    };
    // Options to control the language client
    const clientOptions = {
        // Register the server for plain text documents
        documentSelector: [{ scheme: 'file', language: 'starlark' }],
        synchronize: {
            // Notify the server about file changes to '.clientrc files contained in the workspace
            fileEvents: vscode_1.workspace.createFileSystemWatcher('**.star')
        }
    };
    // Create the language client and start the client.
    client = new node_1.LanguageClient("kurtosis_lsp", 'kurtosis_lsp', () => startServer(file), clientOptions);
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
async function startServer(command) {
    // console.log("Starting Serverrr")
    // if (command !== "") {
    // 	const process = spawn(command)
    // 	process.on("connection", () => {
    // 		console.log("someone connected")
    // 	})
    // 	console.log("PROCESS", process)
    // 	process.stdout.on( 'data', 
    // 		data => console.log( data ) 
    // 	);
    // }
    // const socket = net.connect({ host: "0.0.0.0", port:8567 })
    // return { writer: socket, reader: socket }
    console.log(process.env);
    return (0, child_process_1.spawn)("/Users/preetrawal/go/bin/starlark-lsp", ["start", "--address=", ":8567"]);
}
// /* --------------------------------------------------------------------------------------------
//  * Copyright (c) Microsoft Corporation. All rights reserved.
//  * Licensed under the MIT License. See License.txt in the project root for license information.
//  * ------------------------------------------------------------------------------------------ */
// import * as vscode from 'vscode';
// import net = require("net")
// import { ChildProcess, spawn } from "child_process"
// import {
// 	LanguageClient,
// 	LanguageClientOptions, 
// 	StreamInfo
// } from 'vscode-languageclient/node';
// let client: LanguageClient;
// export function activate(context: vscode.ExtensionContext) {
// 	// Options to control the language client
// 	const clientOptions: LanguageClientOptions = {
// 		// Register the server for plain text documents
// 		documentSelector: [{ scheme: 'file', language: 'starlark' }],
// 		synchronize: {
// 			// Notify the server about file changes to '.clientrc files contained in the workspace
// 			fileEvents: vscode.workspace.createFileSystemWatcher('**.star'),
// 		}
// 	};
// 	// Create the language client and start the client.
// 	client = new LanguageClient(
// 		'languageServerExample',
// 		'Language Server Example PK',
// 		() => startServer(),
// 		clientOptions,
// 	);
// 	// Start the client. This will also launch the server
// 	client.start();
// }
// export function deactivate(): Thenable<void> | undefined {
// 	if (!client) {
// 		return undefined;
// 	}
// 	return client.stop();
// }
//# sourceMappingURL=extension.js.map