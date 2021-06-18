"use strict";

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance"); }

function _iterableToArray(iter) { if (Symbol.iterator in Object(iter) || Object.prototype.toString.call(iter) === "[object Arguments]") return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = new Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _instanceof(left, right) { if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) { return !!right[Symbol.hasInstance](left); } else { return left instanceof right; } }

function _classCallCheck(instance, Constructor) { if (!_instanceof(instance, Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var BASE_URL = 'https://sharemycode.fr'; //'https://sharemycode.fr'
//'http://localhost/sharecode';

/*
 @FredLossignol
 2 Class To Create and Store a sharecodeObject
*/

var SharecodeObject = function SharecodeObject(slug) {
  _classCallCheck(this, SharecodeObject);

  _defineProperty(this, "slug", void 0);

  _defineProperty(this, "created_at", void 0);

  this.slug = slug;
  this.created_at = new Date().getTime();
};
/*
 @FredLossignol
 2 Class USER to create and Store a User
*/


var User =
/*#__PURE__*/
function () {
  function User() {
    _classCallCheck(this, User);

    _defineProperty(this, "preferences", void 0);

    _defineProperty(this, "ip", void 0);

    var user = this.getUser();
    this.preferences = user.preferences;
    this.ip = user.ip;
    this.admin = user.admin;
  }

  _createClass(User, [{
    key: "getUser",
    value: function getUser() {
      if (localStorage.user != undefined) {
        return JSON.parse(localStorage.user);
      } else {
        var user = {
          preferences: {
            theme: 'vscode-dark',
            fontsize: '17px'
          },
          ip: '127.0.0.1',
          admin: false
        };
        localStorage.setItem('user', JSON.stringify(user));
        return user;
      }
    }
  }, {
    key: "setPreferences",
    value: function setPreferences(value) {
      this.preferences = value;
      localStorage.setItem('user', JSON.stringify(this));
    }
  }]);

  return User;
}();
/*
 Class CodeStorage
  data : storedCodes
  public methods : getSharecodes(), saveSharecodeFromUrl(), deleteSharecode(slug)
  private methods: _refreshCodesList(), _eventHandlerOnTrash, _eventHandlerOnSharecodeItem
*/


var CodeStorage =
/*#__PURE__*/
function () {
  // Array of storedCodes in localStorage
  // Date
  // Date
  function CodeStorage() {
    var _this = this;

    _classCallCheck(this, CodeStorage);

    _defineProperty(this, "optionsDate", {
      year: "numeric",
      month: "numeric",
      day: "numeric"
    });

    _defineProperty(this, "storedCodes", []);

    _defineProperty(this, "storedCodesOrderByDate", []);

    _defineProperty(this, "today", new Date());

    _defineProperty(this, "lastSave", void 0);

    _defineProperty(this, "user", void 0);

    this.user = new User();
    this.getSharecodes().then(function (data) {
      _this.storedCodes = data;

      _this.saveSharecodeFromUrl().then(function (res) {
        _this.lastSave = new Date(_this.storedCodes[0].created_at);
        _this.storedCodesOrderByDate = _this.getSharecodesOrderByDate();

        _this._refreshCodesListOrderByDate();
      }); //this.user.setPreferences(themeName, fontSize);

    }); //this.getSharecodesOrderByDate();
  }

  _createClass(CodeStorage, [{
    key: "getSharecodesOrderByDate",
    value: function getSharecodesOrderByDate() {
      var dateOfPreviousCode;
      var codeObject = {};
      var end = [];
      var _iteratorNormalCompletion = true;
      var _didIteratorError = false;
      var _iteratorError = undefined;

      try {
        for (var _iterator = this.storedCodes[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
          var code = _step.value;
          // Pour chaque code on récupere la date sous la forme 18/12/2019
          var date = new Date(code.created_at).toLocaleString('fr-FR', this.optionsDate);
          /*
          * si la date de l'objet code courant est différente de l'objet code précédent
          * on crée un nouvel objet qui contiendra en clé
          * - date : string
          * - shares: Array<code>
          */
          //console.log('code courant', date);
          //console.log('code précédent', dateOfPreviousCode);

          if (date != dateOfPreviousCode) {
            dateOfPreviousCode = date;
            codeObject = {
              date: date,
              shares: []
            };
            codeObject.shares = [].concat(_toConsumableArray(codeObject.shares), [code]);
            end = [].concat(_toConsumableArray(end), [codeObject]);
          } else {
            var index = end.indexOf(codeObject);
            end[index].shares = [].concat(_toConsumableArray(end[index].shares), [code]);
          }
        }
      } catch (err) {
        _didIteratorError = true;
        _iteratorError = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion && _iterator.return != null) {
            _iterator.return();
          }
        } finally {
          if (_didIteratorError) {
            throw _iteratorError;
          }
        }
      }

      return end;
    }
    /*
     getSharecodes():Array<SharecodeObject>
     rôle : get data (sharecodes) from localStorage
     return : array of sharecodes object || array empty
    */

  }, {
    key: "getSharecodes",
    value: async function getSharecodes() {
      var allCodesInStorage = JSON.parse(localStorage.getItem('sharecodes'));

      if (allCodesInStorage == null) {
        return [];
      }

      return allCodesInStorage;
    }
    /*
     saveSharecodeFromUrl():void
     rôle : push one SharecodeObject in sharecodesArray 
     *      and save Array<SharecodeObject> in localStorage 
     *      and refresh listview
    */

  }, {
    key: "saveSharecodeFromUrl",
    value: async function saveSharecodeFromUrl() {
      var indexurl = BASE_URL == 'https://sharemycode.fr' ? 3 : 4;
      var slug = window.location.href.split('/')[indexurl];

      if (slug.length > 3) {
        return;
      }

      if (this.storedCodes.find(function (code) {
        return code.slug == slug;
      }) == undefined) {
        var shareObject = new SharecodeObject(slug);

        if (this.storedCodes.length == 0) {
          this.storedCodes = [shareObject];
        } else {
          this.storedCodes = [shareObject].concat(_toConsumableArray(this.storedCodes));
        }

        localStorage.setItem('sharecodes', JSON.stringify(this.storedCodes));
      }
    }
    /*
     deleteSharecode(slug):void
     rôle : push one SharecodeObject in sharecodesArray 
     *      and save Array<SharecodeObject> in localStorage 
     *      and refresh listview
    */

  }, {
    key: "deleteSharecode",
    value: function deleteSharecode(slug) {
      var codeToRemove = this.storedCodes.find(function (code) {
        return code.slug == slug;
      });
      var index = this.storedCodes.indexOf(codeToRemove);
      this.storedCodes.splice(index, 1);
      localStorage.setItem('sharecodes', JSON.stringify(this.storedCodes));
      this.storedCodesOrderByDate = this.getSharecodesOrderByDate();

      this._refreshCodesListOrderByDate();
    }
  }, {
    key: "_refreshCodesList",
    value: function _refreshCodesList() {
      var indexurl = BASE_URL == 'https://sharemycode.fr' ? 3 : 4;
      var slugInUrl = window.location.href.split('/')[indexurl];
      var codeslistElt = document.querySelector('div.codelist');
      console.log('slugInUrl');

      if (this.storedCodes.length > 0) {
        codeslistElt.innerHTML = '';
        var ulElt = document.createElement('ul');
        var _iteratorNormalCompletion2 = true;
        var _didIteratorError2 = false;
        var _iteratorError2 = undefined;

        try {
          for (var _iterator2 = this.storedCodes[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
            var code = _step2.value;
            ulElt.innerHTML += "\n    <li class=\"".concat(slugInUrl === code.slug ? 'same' : '', "\" data-slug='").concat(code.slug, "'>\n     sharemycode.fr/<span>").concat(code.slug, "</span>\n     <button data-slug='").concat(code.slug, "' class='deletecode'>\n      <svg class=\"icon icon-bin\">\n       <use xlink:href=\"res/css/icon.svg#icon-bin\"></use>\n      </svg>\n     </button>\n    </li>");
          }
        } catch (err) {
          _didIteratorError2 = true;
          _iteratorError2 = err;
        } finally {
          try {
            if (!_iteratorNormalCompletion2 && _iterator2.return != null) {
              _iterator2.return();
            }
          } finally {
            if (_didIteratorError2) {
              throw _iteratorError2;
            }
          }
        }

        codeslistElt.appendChild(ulElt);

        this._eventHandlerOnSharecodeItem(document.querySelectorAll('.codelist ul li'));

        this._eventHandlerOnTrash(document.querySelectorAll('.codelist ul li button'));
      } else {
        codeslistElt.innerHTML = "";
      }
    }
  }, {
    key: "_refreshCodesListOrderByDate",
    value: function _refreshCodesListOrderByDate() {
      var indexurl = BASE_URL == 'https://sharemycode.fr' ? 3 : 4;
      var slugInUrl = window.location.href.split('/')[indexurl];
      var codeslistElt = document.querySelector('div.codelist');

      if (this.storedCodesOrderByDate.length > 0) {
        codeslistElt.innerHTML = '';
        var _iteratorNormalCompletion3 = true;
        var _didIteratorError3 = false;
        var _iteratorError3 = undefined;

        try {
          for (var _iterator3 = this.storedCodesOrderByDate[Symbol.iterator](), _step3; !(_iteratorNormalCompletion3 = (_step3 = _iterator3.next()).done); _iteratorNormalCompletion3 = true) {
            var codeListByDate = _step3.value;
            var ulElt = document.createElement('ul');
            var dateTitleElth2 = document.createElement('h2');
            dateTitleElth2.textContent = codeListByDate.date;
            var _iteratorNormalCompletion4 = true;
            var _didIteratorError4 = false;
            var _iteratorError4 = undefined;

            try {
              for (var _iterator4 = codeListByDate.shares[Symbol.iterator](), _step4; !(_iteratorNormalCompletion4 = (_step4 = _iterator4.next()).done); _iteratorNormalCompletion4 = true) {
                var code = _step4.value;
                ulElt.innerHTML += "\n     <li data-slug='".concat(code.slug, "'>\n      <span>\n       <svg class=\"icon icon-point ").concat(slugInUrl === code.slug ? 'same' : '', "\">\n       <use xlink:href=\"res/css/icon.svg#icon-point\"></use>\n       </svg>\n      </span>\n      sharemycode.fr/<span>").concat(code.slug, "</span>\n      <button data-slug='").concat(code.slug, "' class='deletecode'>\n       <svg class=\"icon icon-bin\">\n        <use xlink:href=\"res/css/icon.svg#icon-bin\"></use>\n       </svg>\n      </button>\n     </li>");
              }
            } catch (err) {
              _didIteratorError4 = true;
              _iteratorError4 = err;
            } finally {
              try {
                if (!_iteratorNormalCompletion4 && _iterator4.return != null) {
                  _iterator4.return();
                }
              } finally {
                if (_didIteratorError4) {
                  throw _iteratorError4;
                }
              }
            }

            codeslistElt.appendChild(dateTitleElth2);
            codeslistElt.appendChild(ulElt);
          }
        } catch (err) {
          _didIteratorError3 = true;
          _iteratorError3 = err;
        } finally {
          try {
            if (!_iteratorNormalCompletion3 && _iterator3.return != null) {
              _iterator3.return();
            }
          } finally {
            if (_didIteratorError3) {
              throw _iteratorError3;
            }
          }
        }

        this._eventHandlerOnSharecodeItem(document.querySelectorAll('.codelist ul li'));

        this._eventHandlerOnTrash(document.querySelectorAll('.codelist ul li button'));
      } else {
        codeslistElt.innerHTML = "";
      }
    }
  }, {
    key: "_eventHandlerOnTrash",
    value: function _eventHandlerOnTrash(trashBtns) {
      var _this2 = this;

      var _iteratorNormalCompletion5 = true;
      var _didIteratorError5 = false;
      var _iteratorError5 = undefined;

      try {
        for (var _iterator5 = trashBtns[Symbol.iterator](), _step5; !(_iteratorNormalCompletion5 = (_step5 = _iterator5.next()).done); _iteratorNormalCompletion5 = true) {
          var trashBtn = _step5.value;
          trashBtn.addEventListener('click', function (event) {
            event.stopPropagation();

            _this2.deleteSharecode(event.currentTarget.dataset.slug);
          });
        }
      } catch (err) {
        _didIteratorError5 = true;
        _iteratorError5 = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion5 && _iterator5.return != null) {
            _iterator5.return();
          }
        } finally {
          if (_didIteratorError5) {
            throw _iteratorError5;
          }
        }
      }
    }
  }, {
    key: "_eventHandlerOnSharecodeItem",
    value: function _eventHandlerOnSharecodeItem(liElts) {
      var _iteratorNormalCompletion6 = true;
      var _didIteratorError6 = false;
      var _iteratorError6 = undefined;

      try {
        for (var _iterator6 = liElts[Symbol.iterator](), _step6; !(_iteratorNormalCompletion6 = (_step6 = _iterator6.next()).done); _iteratorNormalCompletion6 = true) {
          var item = _step6.value;
          item.addEventListener('click', function () {
            window.location.href = BASE_URL + '/' + event.currentTarget.dataset.slug;
          });
        }
      } catch (err) {
        _didIteratorError6 = true;
        _iteratorError6 = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion6 && _iterator6.return != null) {
            _iterator6.return();
          }
        } finally {
          if (_didIteratorError6) {
            throw _iteratorError6;
          }
        }
      }
    }
  }]);

  return CodeStorage;
}();