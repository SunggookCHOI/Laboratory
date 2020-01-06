"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const sequelize_1 = require("sequelize");
const friend_1 = __importDefault(require("./friend"));
const config_1 = __importDefault(require("../config/config"));
function init() {
    const sequelize = new sequelize_1.Sequelize(config_1.default.mysql.key);
    friend_1.default.init({
        id: {
            type: sequelize_1.DataTypes.INTEGER.UNSIGNED,
            autoIncrement: true,
            primaryKey: true,
        },
        name: {
            type: new sequelize_1.DataTypes.STRING(128),
            allowNull: false,
        },
        hobby: {
            type: new sequelize_1.DataTypes.STRING(128),
            allowNull: true,
        }
    }, {
        sequelize,
        tableName: 'people',
        timestamps: false,
        freezeTableName: true,
    });
    return sequelize;
}
exports.init = init;
