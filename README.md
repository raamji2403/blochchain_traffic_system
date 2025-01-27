# Blockchain Based Traffic Light System

This project tracks the change of traffic signal of each pole in blockchain using Ganache.

## Table of Contents
- [Repository Structure](#repository-structure)
- [Truffle Set-up](#truffle-set-up)
- [Ganache Set-up](#ganache-set-up)
- [Final Set-up](#final-set-up)

### Note : Before initializing truffle make sure the system's execution policy is Remoted-Signed.
## Repository Structure
blockchain_traffic_system/<br>
├── build/contracts<br>
&nbsp;&nbsp;&nbsp;&nbsp; ├── Traffic.json<br>
├── contracts<br>
&nbsp;&nbsp;&nbsp;&nbsp; ├── Traffic.sol<br>
├── migrations<br>
&nbsp;&nbsp;&nbsp;&nbsp; ├── 2deploy_contract.js<br>
├── static<br>
&nbsp;&nbsp;&nbsp;&nbsp; ├── style.css<br>
├── templates<br>
&nbsp;&nbsp;&nbsp;&nbsp; ├── index.html<br>
├── app.py<br>
├── compiled_contract.json<br>
├── truffle-config.js

## Truffle Set-Up
  1. Open terminal to blockchain_traffic_system directory.<br>
  2. Run the command to initialize truffle
     ```bash
       truffle init
     ```
  3. After that ,[ truffle_config.js  , /contracts , /migrations , /tests] 3 folder  and 1 file will be generated.<br>
  4. In truffle-config.js , un-command the deployment part and change the port to 7545 where Ganache blockchain runs in background.<br>
  5. Put the Traffic.sol in /contracts directory and 2deploy_contract.js in /migrations directory.<br>
  6. To compile the contract run
     ```bash
       truffle compile
     ```
  7. After that , /build/contracts/Traffic.json will be created and copy that to compiled_contract.json.

## Ganache Set-Up
1. Download & install Ganache
2. Click on "NEW WORKSPACE"
3. Give "Work Space Name"(top-left).
4. Click "ADD PROJECT"(bottom-left) and select the "truffle-config.js" file.
5. Go to "ACCOUNT & KEYS" section and give "ACCOUNT DEFAULT BALANCE" and "TOTAL ACCOUNTS TO GENERATE".
6. Click "START" button on the top-right.
7. Run the command in terminal to deploy contract
     ```bash
       truffle migrate
     ```
## Final Set-Up
1. After deployment of contract, copy the contract address and add it in  app.py .
2.  Open VS Code in terminal to blockchain_traffic_system and run
     ```bash
       python app.py
     ```
3. Click the local or network URL to interact with UI.
   
## Contributing
Contributions are welcome! Please feel free to open issues or pull requests for any improvements or features.
