class PostDataStructure {
    constructor() {
        this.id = null;
        this.user_id = null
        this.username = null
        this.post = null
        this.like_count = null
        this.created_at = null
        this.updated_at = null
    }

    static fromArray(data) {
        return _.assign(new PostDataStructure(), data);
    }
}

export {PostDataStructure}