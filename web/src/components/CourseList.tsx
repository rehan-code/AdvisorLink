import React from 'react';

interface IProps {
}

interface IState {
    sections: any[]
}

class CourseList extends React.Component<IProps, IState>{

    constructor(props: IProps) {
        super(props);
        this.fetchAllData();
        this.state = {
            sections: []
        }
    }

    async fetchAllData() {
        await fetch('/api/sections', {
            method: 'GET',
        })
            .then(data => data.json())
            .then((data) => {
                this.setState(data);
            })
    }

    createRow(section: any) {
        // Change this: create components for each section.
        return (
            <li key={section.faculty + section.code + section.number}>
                {section.name}
            </li>
        );
    }

    createList() {
        // Change this
        return (
            <ul className="courseList">
                {this.state.sections.map(section => { return this.createRow(section) })}
            </ul>
        )
    }

    render() {
        return (
            <>
                {this.createList()}
            </>
        );
    }
}

export default CourseList;
