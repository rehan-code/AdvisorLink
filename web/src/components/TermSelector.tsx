import React from 'react';

export interface TermSelectorProps {
  setValue?: any;
  setTerm?: any;
}

export function TermSelector(props: TermSelectorProps) {
  const { setValue, setTerm } = props;

  const [terms, setTerms] = React.useState<any[]>([]);
  const [selectedId, setSelectedId] = React.useState<string>('');
  const [loaded, setLoaded] = React.useState(false);

  const onValueChange = (id: string) => {
    setSelectedId(id);
    setValue?.(id);
    setTerm?.(terms.find((t) => t.id === id));
  };

  /* Load the terms stored in the database when the component is first rendered. */
  const loadOptions = async () => {
    const response = await fetch(`/api/terms`);

    if (response.status >= 400)
      throw new Error(
        `Failed to retrieve term data from server (${response.status}: ${response.statusText})`,
      );

    const { terms: ts } = await response.json();
    setTerms(ts);
    setLoaded(true);
    onValueChange(ts[0].id);
  };
  React.useEffect(() => {
    loadOptions().catch((e) => alert(e));
  }, []);

  if (!loaded)
    return (
      <select
        className="py-4 px-8 bg-blue-800 rounded-md text-white font-bold"
        style={{
          color: 'white',
          fontWeight: 'bold',
          textAlign: 'center',
        }}
        onClick={(e: any) => {
          e.preventDefault();
          e.stopPropagation();
        }}
        disabled
      >
        {' '}
      </select>
    );

  return (
    <select
      className="py-4 px-8 bg-blue-800 rounded-md text-white hover:bg-blue-900 font-bold"
      style={{
        color: 'white',
        fontWeight: 'bold',
        textAlign: 'center',
      }}
      onClick={(e: any) => {
        e.preventDefault();
        e.stopPropagation();
      }}
      onChange={(e) => onValueChange(e.target.value)}
      value={selectedId}
    >
      {terms.map((t) => (
        <option value={t.id} key={t.id}>
          {t.name}
        </option>
      ))}
    </select>
  );
}
