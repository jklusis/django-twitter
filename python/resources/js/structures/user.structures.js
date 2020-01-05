class UserDataStructure {
    constructor() {
        this.username = null
        this.email = null
        this.first_name = null
        this.last_name = null
        this.date_joined = null
        this.following_count = null
        this.follower_count = null
        this.post_count = null
    }

    static fromArray(data) {
        return _.assign(new UserDataStructure(), data);
    }
}

export {UserDataStructure}