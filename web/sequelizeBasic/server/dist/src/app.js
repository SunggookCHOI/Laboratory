"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const friend_1 = __importDefault(require("../models/friend"));
const DB = __importStar(require("../models/index"));
const body_parser_1 = __importDefault(require("body-parser"));
const mysql = DB.init();
const app = express_1.default();
app.use(body_parser_1.default.json());
app.get('/users', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const temp = yield friend_1.default.findAll({
        attributes: ['name', 'hobby'],
        raw: true
    }).then(function () {
        console.log(arguments);
        res.json(temp);
    }).catch(function (e) {
        res.status(400).send(e.message);
    });
}));
app.get('/user/:id', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
}));
app.post('/user', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const body = req.body;
    const newPeople = yield friend_1.default.create({
        name: body.name,
        hobby: body.hobby
    }).then(function () {
        console.log(arguments);
        res.json({ ok: true });
    }).catch(function (e) {
        res.status(400).send(e.message);
    });
}));
app.delete('/user/:id', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    yield friend_1.default.destroy({ where: { id: req.params.id } })
        .then(function () {
        console.log(arguments);
        res.json({ ok: true });
    })
        .catch(function (e) {
        res.status(400).send(e.message);
    });
}));
app.listen(7878, function () {
    console.log('The server has started on port 7878');
});
